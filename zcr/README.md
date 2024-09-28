zero copy read implemented in rust

bench results
```
Running benches/zcr_bench.rs (rust/misc_rust/target/release/deps/zcr_bench-7c7acc17ed3d44c4)
Gnuplot not found, using plotters backend
bench_normal            time:   [17.604 ms 17.804 ms 18.017 ms]
                        change: [-2.1957% -0.6232% +0.9695%] (p = 0.46 > 0.05)
                        No change in performance detected.
Found 1 outliers among 100 measurements (1.00%)
  1 (1.00%) high severe

Benchmarking bench_zero_copy: Warming up for 3.0000 s
Warning: Unable to complete 100 samples in 5.0s. You may wish to increase target time to 6.3s, enable flat sampling, or reduce sample count to 60.
bench_zero_copy         time:   [1.2134 ms 1.2309 ms 1.2499 ms]
                        change: [+13.076% +14.733% +16.332%] (p = 0.00 < 0.05)
                        Performance has regressed.
```