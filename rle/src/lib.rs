use core::fmt;
use std::string;

// writing custom err
// https://doc.rust-lang.org/rust-by-example/error/multiple_error_types/define_error_type.html
#[derive(Debug, Clone, PartialEq)] // NOTE not sure why PartialEq is required
pub struct CustomError;
impl fmt::Display for CustomError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Length of input must be at least 1")
    }
}

pub fn rle_encode(input: &str) -> Result<string::String, CustomError> {
    let len_input = input.chars().count();
    if len_input < 1 {
        return Err(CustomError);
    }

    let mut output = string::String::new();
    let mut input_char_iter = input.chars();
    // pop current 
    let mut last = input_char_iter.next().unwrap();
    let mut curr_len = 1;
    while let Some(c) = input_char_iter.next() {
        if c != last {
            let section_res = format!("{}{}", curr_len, last);
            output.push_str(&section_res);
            curr_len = 1;
            last = c;
            continue;
        }

        // else
        curr_len += 1;
    }

    // gotta do it at the end too
    let section_res = format!("{}{}", curr_len, last);
    output.push_str(&section_res);

    Ok(output)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case1() {
        let res = rle_encode("aaaabbbbccc").unwrap();
        assert_eq!(res, "4a4b3c");
    }

    #[test]
    fn case2() {
        let res = rle_encode("zabcdefgaaaa").unwrap();
        assert_eq!(res, "1z1a1b1c1d1e1f1g4a");
    }

    #[test]
    fn case3() {
        let res = rle_encode("-!@#$())").unwrap();
        assert_eq!(res, "1-1!1@1#1$1(2)")
    }

    #[test]
    fn case4() {
        let res = rle_encode("a").unwrap();
        assert_eq!(res, "1a");
    }

    #[test]
    fn err_case1() {
        let err = rle_encode("").unwrap_err();
        assert_eq!(err, CustomError);
    }
}
