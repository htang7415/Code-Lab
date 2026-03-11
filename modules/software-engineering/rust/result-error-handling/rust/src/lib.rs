#[derive(Debug, PartialEq, Eq)]
pub enum ParsePortError {
    Empty,
    Invalid,
    OutOfRange,
    InvalidHost,
}

pub fn parse_port(input: &str) -> Result<u16, ParsePortError> {
    let trimmed = input.trim();
    if trimmed.is_empty() {
        return Err(ParsePortError::Empty);
    }

    let value: u32 = trimmed.parse().map_err(|_| ParsePortError::Invalid)?;
    if value > u16::MAX as u32 {
        return Err(ParsePortError::OutOfRange);
    }
    Ok(value as u16)
}

pub fn bind_address(host: &str, port: &str) -> Result<String, ParsePortError> {
    let cleaned_host = host.trim();
    if cleaned_host.is_empty() {
        return Err(ParsePortError::InvalidHost);
    }
    let parsed_port = parse_port(port)?;
    Ok(format!("{cleaned_host}:{parsed_port}"))
}
