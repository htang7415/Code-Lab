use software_engineering_rust_result_error_handling::{bind_address, parse_port, ParsePortError};

#[test]
fn test_parse_port_accepts_valid_values() {
    assert_eq!(parse_port("8080"), Ok(8080));
    assert_eq!(bind_address("127.0.0.1", "8080"), Ok(String::from("127.0.0.1:8080")));
}

#[test]
fn test_parse_port_rejects_empty_invalid_and_out_of_range_values() {
    assert_eq!(parse_port(""), Err(ParsePortError::Empty));
    assert_eq!(parse_port("abc"), Err(ParsePortError::Invalid));
    assert_eq!(parse_port("70000"), Err(ParsePortError::OutOfRange));
}

#[test]
fn test_bind_address_rejects_blank_host() {
    assert_eq!(bind_address(" ", "8080"), Err(ParsePortError::InvalidHost));
}
