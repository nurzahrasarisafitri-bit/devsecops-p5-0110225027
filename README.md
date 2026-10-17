# Task Manager — DevSecOps

## Deskripsi Aplikasi
Task Manager adalah aplikasi berbasis Python untuk menambahkan, menampilkan, dan menghapus daftar tugas melalui terminal.

## Teknologi
- Python
- unittest untuk pengujian otomatis
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk otomatisasi CI/CD

## Cara Menjalankan Aplikasi
Pastikan Python sudah terinstal, kemudian jalankan perintah berikut:

```bash
python -m app.cli
```

## Cara Menjalankan Pengujian
```bash
python -m unittest discover -s tests -v
```

## Pipeline CI/CD
Workflow GitHub Actions dijalankan ketika terjadi push ke branch `main` atau pull request menuju branch `main`. Pipeline menjalankan job build dan test, kemudian melakukan pemindaian keamanan kode Python menggunakan Bandit. Hasil pemindaian digunakan untuk menentukan apakah Quality Gate terpenuhi.
