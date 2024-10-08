// learning zero copy reads
// https://medium.com/@emreeaydiinn/zero-copy-reads-explained-8d54e6084857
// https://blog.devgenius.io/linux-zero-copy-d61d712813fe

use std::fs::{self, File};
use std::io;
use std::io::{BufReader, BufWriter, Read, Write};

use memmap2::Mmap;

// https://users.rust-lang.org/t/rust-file-open-error-handling/50681/2
// .map_err(|_| "Could not read")
// &'static str

// https://doc.rust-lang.org/std/result/#:~:text=Result%20is,and%20containing%20an%20error%20value.&text=Functions%20return%20Result%20whenever%20errors%20are%20expected%20and%20recoverable.
pub fn normal_copy(from: &str, to: &str) -> Result<bool, io::Error> {
    // open source file
    let input_file = File::open(from)
        .map_err(|_| io::Error::new(io::ErrorKind::NotFound, "input file not found"))?;

    let mut reader = BufReader::new(input_file);

    // open dest for writing
    let out_file = File::create(to)?;
    let mut writer = BufWriter::new(out_file);

    // Create a buffer and copy data in chunks
    let mut buffer = Vec::with_capacity(1024);
    reader.read_to_end(&mut buffer)?;
    writer.write_all(&buffer)?;

    // success
    Ok(true)
}

pub fn zero_copy(from: &str, to: &str) -> Result<bool, io::Error> {
    // open source file
    let input_file = File::open(from)
        .map_err(|_| io::Error::new(io::ErrorKind::NotFound, "input file not found"))?;

    // mmap
    // assumes there is NO concurrent access
    // otherwise a mutex is required
    let mmap = unsafe { Mmap::map(&input_file)? };
    let data = &mmap[..];

    // https://stackoverflow.com/a/65703152
    // basically a new and better way of implementing
    // the same write functionality
    // from the normal_copy BufWriter, etc
    let mut new_file = fs::OpenOptions::new()
        .create(true) // creates new file
        .write(true) // allows write
        .open(to)?;

    new_file.write_all(data)?;

    Ok(true)
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::env;

    #[test]
    fn normal_copy_works() {
        // print current path
        let path = env::current_dir().unwrap();
        println!("Currdir: {}", path.display());

        // testing fn
        let ok = normal_copy("seed/file.csv", "test_out/new.csv");
        assert!(ok.is_ok());
        let is_success = ok.unwrap();
        assert_eq!(is_success, true);
    }

    #[test]
    fn zero_copy_works() {
        // testing fn
        let ok = zero_copy("seed/file.csv", "test_out/zero_c.csv");
        assert!(ok.is_ok());
        let is_success = ok.unwrap();
        assert_eq!(is_success, true);
    }
}
