use pyo3::prelude::*;
use regex::Regex;

fn rust_regex_nogil(contents: &str, regex_pattern: &str) -> Option<String> {
    let re = Regex::new(regex_pattern).ok()?; // returns None if regex compilation fails
    re.find(contents).map(|m| m.as_str().to_string()) // automatically returns
}

#[pyfunction]
fn regex_match(py: Python<'_>, contents: &str, regex_pattern: &str) -> PyResult<Option<String>>{
    let result = py.allow_threads(|| rust_regex_nogil(contents, regex_pattern));
    Ok(result)
}


#[pymodule]
fn rust_regex(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(regex_match, m)?)?;
    Ok(())
}
