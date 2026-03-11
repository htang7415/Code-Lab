use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll, RawWaker, RawWakerVTable, Waker};

pub async fn concurrency_budget(worker_count: usize, per_worker_in_flight: usize) -> usize {
    worker_count * per_worker_in_flight
}

pub fn async_service_fit(network_wait_ms: u64, cpu_ms: u64) -> bool {
    network_wait_ms > cpu_ms
}

pub fn backpressure_needed(in_flight: usize, budget: usize) -> bool {
    in_flight > budget
}

fn dummy_raw_waker() -> RawWaker {
    fn clone(_: *const ()) -> RawWaker {
        dummy_raw_waker()
    }
    fn wake(_: *const ()) {}
    fn wake_by_ref(_: *const ()) {}
    fn drop(_: *const ()) {}

    RawWaker::new(
        std::ptr::null(),
        &RawWakerVTable::new(clone, wake, wake_by_ref, drop),
    )
}

fn dummy_waker() -> Waker {
    unsafe { Waker::from_raw(dummy_raw_waker()) }
}

pub fn block_on_ready<F: Future>(future: F) -> F::Output {
    let waker = dummy_waker();
    let mut context = Context::from_waker(&waker);
    let mut future = Box::pin(future);

    loop {
        match Pin::as_mut(&mut future).poll(&mut context) {
            Poll::Ready(output) => return output,
            Poll::Pending => continue,
        }
    }
}
