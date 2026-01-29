use two_sum::two_sum;

#[test]
fn test_example_1() {
    let mut result = two_sum(&[2, 7, 11, 15], 9);
    result.sort();
    assert_eq!(result, vec![0, 1]);
}

#[test]
fn test_example_2() {
    let mut result = two_sum(&[3, 2, 4], 6);
    result.sort();
    assert_eq!(result, vec![1, 2]);
}

#[test]
fn test_duplicates() {
    let mut result = two_sum(&[3, 3], 6);
    result.sort();
    assert_eq!(result, vec![0, 1]);
}

#[test]
fn test_negative_numbers() {
    let mut result = two_sum(&[-1, -2, -3, -4, -5], -8);
    result.sort();
    assert_eq!(result, vec![2, 4]);
}
