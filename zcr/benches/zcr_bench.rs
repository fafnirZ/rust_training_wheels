// benchmarks with criterion
// https://medium.com/rustaceans/benchmarking-your-rust-code-with-criterion-a-comprehensive-guide-fa38366870a6
// https://bencher.dev/learn/benchmarking/rust/criterion/

use criterion::{criterion_group, criterion_main, Criterion};
use zcr::*;


fn bench_normal(c: &mut Criterion) {
  c.bench_function("bench_normal", |b| {
    b.iter(|| {
      std::hint::black_box(for i in 1..=100 {
        let _ = zcr::normal_copy("seed/file.csv", "test_out/normal.csv");
      })
    })
  });
}

fn bench_zc(c: &mut Criterion) {
  c.bench_function("bench_zero_copy", |b| {
    b.iter(|| {
      std::hint::black_box(for i in 1..=100 {
        let _ = zcr::zero_copy("seed/file.csv", "test_out/zero_c.csv");
      })
    })
  });
}

criterion_group!(
  benches,
  bench_normal,
  bench_zc,
);

criterion_main!(benches);