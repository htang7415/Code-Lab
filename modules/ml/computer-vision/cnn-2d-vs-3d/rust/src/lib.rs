pub fn output_depth(input_depth: i32, kernel_depth: i32) -> i32 {
    input_depth - kernel_depth + 1
}
