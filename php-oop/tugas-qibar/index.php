<?php
$hasil = "";

if (isset($_GET['hitung'])) {
    $angka1 = $_GET['angka1'];
    $angka2 = $_GET['angka2'];
    $operasi = $_GET['operasi'];

    if ($angka1 !== "" && $angka2 !== "") {
        if ($operasi == "tambah") {
            $hasil = $angka1 + $angka2;
        } elseif ($operasi == "kurang") {
            $hasil = $angka1 - $angka2;
        } elseif ($operasi == "kali") {
            $hasil = $angka1 * $angka2;
        } elseif ($operasi == "bagi") {
            // Cek pembagian nol
            if ($angka2 == 0) {
                $hasil = "angka tidak bisa dibagi";
            } else {
                $hasil = $angka1 / $angka2;
            }
        }
    } else {
        $hasil = "Isi semua angka!";
    }
}
?>
<html>
<head>
    <title>Kalkulator Sederhana</title>
</head>
<body>

    <h2>Kalkulator</h2>

    <form method="GET" action="">
        <input type="number" name="angka1" value="<?php echo isset($_GET['angka1']) ? $_GET['angka1'] : ''; ?>">
        
        <select name="operasi">
            <option value="tambah">+</option>
            <option value="kurang">-</option>
            <option value="kali">x</option>
            <option value="bagi">/</option>
        </select>

        <input type="number" name="angka2" value="<?php echo isset($_GET['angka2']) ? $_GET['angka2'] : ''; ?>">
        
        <button type="submit" name="hitung">Hitung</button>
    </form>

    <?php if ($hasil !== ""): ?>
        <h4>Hasil: <?php echo $hasil; ?></h4>
    <?php endif; ?>

</body>
</html>
