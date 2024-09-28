// learning zero copy reads
// https://medium.com/@emreeaydiinn/zero-copy-reads-explained-8d54e6084857
// https://blog.devgenius.io/linux-zero-copy-d61d712813fe

use std::fs::File;
use std::io::{self, BufReader, BufWriter, Read, Write};

// yes I know there is a std::io::copy command
// https://chatgpt.com/share/66f7eb2d-a4e0-800c-a4e2-4c8d3207d5f1
pub fn normal_copy(from: &str, to: &str) {
    // open source file
    let input_file = File::open(from)?;
    let mut reader = BufReader::new(input_file);

    // open dest for writing
    let out_file = File::create(to)?;
    let mut writer = BufWriter::new(out_file);


    // does it automatically close the fil
}



#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn works() {

    }
}