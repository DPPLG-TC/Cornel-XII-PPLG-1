<?php
// --- BAGIAN LOGIKA (PHP) ---

// Inisialisasi variabel default
$angka1 = "";
$angka2 = "";
$operasi = "";
$hasil = null;
$pesan = "";

// Cek apakah form telah disubmit
if (isset($_POST['hitung'])) {
    $angka1 = $_POST['angka1'];
    $angka2 = $_POST['angka2'];
    $operasi = $_POST['operasi'];

    switch ($operasi) {
        case 'tambah':
            $hasil = $angka1 + $angka2;
            break;
        case 'kurang':
            $hasil = $angka1 - $angka2;
            break;
        case 'kali':
            $hasil = $angka1 * $angka2;
            break;
        case 'bagi':
            if ($angka2 != 0) {
                $hasil = $angka1 / $angka2;
            } else {
                $pesan = "Error: Tidak bisa membagi dengan nol!";
            }
            break;
        default:
            $pesan = "Operasi tidak valid";
            break;
    }
}
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator Sederhana PHP</title>
</head>
<body>
    <!-- --- BAGIAN TAMPILAN (HTML) --- -->
    <h2>Kalkulator Sederhana</h2>
    
    <form method="post" action="">
        <input type="number" name="angka1" placeholder="Masukkan Angka Pertama" required step="any" value="<?php echo htmlspecialchars($angka1); ?>">
        <br><br>
        
        <select name="operasi">
            <option value="tambah" <?php if($operasi == 'tambah') echo 'selected'; ?>>Ditambah (+)</option>
            <option value="kurang" <?php if($operasi == 'kurang') echo 'selected'; ?>>Dikurang (-)</option>
            <option value="kali" <?php if($operasi == 'kali') echo 'selected'; ?>>Dikali (x)</option>
            <option value="bagi" <?php if($operasi == 'bagi') echo 'selected'; ?>>Dibagi (/)</option>
        </select>
        <br><br>
        
        <input type="number" name="angka2" placeholder="Masukkan Angka Kedua" required step="any" value="<?php echo htmlspecialchars($angka2); ?>">
        <br><br>
        
        <button type="submit" name="hitung">Hitung</button>
    </form>
    <br>

    <?php if ($pesan != ""): ?>
        <div><?php echo $pesan; ?></div>
    <?php elseif ($hasil !== null): ?>
        <div>Hasil: <?php echo $hasil; ?></div>
    <?php endif; ?>
</body>
</html>
