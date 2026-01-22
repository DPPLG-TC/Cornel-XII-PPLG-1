<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator Sederhana</title>
</head>
<body>
    <h1>Kalkulator Sederhana</h1>
    <form action="" method="post">
        <label for="angka1">Angka 1</label>
        <input type="number" name="angka1" id="angka1" required>
        <br><br>
        <label for="operasi">Operasi</label>
        <select name="operasi" id="operasi">
            <option value="tambah">+</option>
            <option value="kurang">-</option>
            <option value="kali">*</option>
            <option value="bagi">/</option>
        </select>
        <br><br>
        <label for="angka2">Angka 2</label>
        <input type="number" name="angka2" id="angka2" required>
        <br><br>
        <button type="submit" name="hitung">Hitung</button>
    </form>

    <?php
    function hitung($angka1, $angka2, $operasi) {
        $hasil = 0;
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
                    $hasil = "Tidak bisa dibagi dengan nol";
                }
                break;
        }
        return $hasil;
    }

    if (isset($_POST['hitung'])) {
        $angka1 = $_POST['angka1'];
        $angka2 = $_POST['angka2'];
        $operasi = $_POST['operasi'];
        
        $hasil = hitung($angka1, $angka2, $operasi);

        echo "<h3>Hasil: $hasil</h3>";
    }
    ?>
</body>
</html>