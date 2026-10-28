fn main() {
    println!("cargo:rerun-if-changed=build.rs");

    // macOSではdylibのinstall nameがリンク先の実行ファイルに記録され、実行時にはそのパスから探される。デフォルトだとビ
    // ルド時の絶対パス(例: `/Users/runner/work/…/libvoicevox_core.dylib`)になってしまい、配布先では見つからない。
    // そのため、`@rpath`からの相対にしておく。
    if std::env::var("CARGO_CFG_TARGET_OS").unwrap() == "macos" {
        println!("cargo:rustc-cdylib-link-arg=-Wl,-install_name,@rpath/libvoicevox_core.dylib");
    }
}
