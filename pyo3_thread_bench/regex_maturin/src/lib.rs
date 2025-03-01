use pyo3::prelude::*;
use regex::Regex;

fn rust_regex_nogil(contents: &str, regex_pattern: &str) -> Option<Vec<String>> {
    let re = Regex::new(regex_pattern).ok()?; // returns None if regex compilation fails
    let matches: Vec<String> = re.find_iter(contents)
                                    .map(|m| m.as_str().to_string())
                                    .collect();

    if matches.is_empty() {
        None
    } else {
        Some(matches)
    }
}

fn rust_regex_nogil_indices(contents: &str, regex_pattern: &str) -> Option<Vec<(usize, usize)>> {
    let re = Regex::new(regex_pattern).ok()?;
    let matches: Vec<(usize, usize)> = re
        .find_iter(contents)
        .map(|m| (m.start(), m.end()))
        .collect();

    if matches.is_empty() {
        None
    } else {
        Some(matches)
    }
}

#[pyfunction]
fn regex_match(py: Python<'_>, contents: &str, regex_pattern: &str) -> PyResult<Option<Vec<String>>>{
    let result = py.allow_threads(|| rust_regex_nogil(contents, regex_pattern));
    Ok(result)
}
#[pyfunction]
fn regex_match_index(py: Python<'_>, contents: &str, regex_pattern: &str) -> PyResult<Option<Vec<(usize, usize)>>>{
    let result = py.allow_threads(|| rust_regex_nogil_indices(contents, regex_pattern));
    Ok(result)
}


// https://pyo3.rs/main/getting-started.html?#running-code
/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn regex_maturin(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(regex_match, m)?);
    m.add_function(wrap_pyfunction!(regex_match_index, m)?);
    Ok(())
}
