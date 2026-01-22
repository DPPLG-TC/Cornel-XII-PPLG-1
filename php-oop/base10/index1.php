<?php
function ambil_input($nama) {
    return isset($_GET[$nama]) && $_GET[$nama] !== '' ? (float)$_GET[$nama] : 0;
}

function hitung($a, $b, $operasi) {
    switch ($operasi) {
        case 'Tambah': return $a + $b;
        case 'Kurang': return $a - $b;
        case 'Kali':   return $a * $b;
        case 'Bagi':   return $b != 0 ? $a / $b : 'Error (Bagi 0)';
        default:       return 0;
    }
}

$n1 = ambil_input('angka1');
$n2 = ambil_input('angka2');
$tombol = isset($_GET['operasi']) ? $_GET['operasi'] : '';
$hasil = hitung($n1, $n2, $tombol);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Kalkulator Sederhana</title>
</head>
<body>
    <h3>Kalkulator PHP</h3>
    <p>Angka 1: <?= $n1 ?></p>
    <p>Angka 2: <?= $n2 ?></p>
    <p><b>Hasil (<?= $tombol ?>): <?= $hasil ?></b></p>
    
    <hr>
    
    <form method="get">
        <input type="number" name="angka1" placeholder="Angka 1" required>
        <br>
        <input type="number" name="angka2" placeholder="Angka 2" required>
        <br><br>
        <input type="submit" name="operasi" value="Tambah">
        <input type="submit" name="operasi" value="Kurang">
        <input type="submit" name="operasi" value="Kali">
        <input type="submit" name="operasi" value="Bagi">
    </form>
</body>
</html>
