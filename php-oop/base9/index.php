<?php

function get_data($data){
    if(isset($_GET[$data])){
        return $_GET[$data];
    }else{
        return "tidak ada data";
    }
}

?>

<html>
    <head>
        <title>Cek Nilai USK</title>
    </head>
    <body>
<?php 
        // Cek dulu apakah 'nama' dan 'nilai' sudah ada (tombol sudah ditekan)
        if(isset($_GET['nama']) && isset($_GET['nilai'])) { 
        ?>
        <h1><?php echo get_data('nama') ;?></h1>
        <h1><?php 
        $nilai = get_data('nilai');
        if($nilai >= 78){
            echo "anda lulus! nilai = ", $nilai;
        }else{
            echo "anda tidak lulus! nilai = ", $nilai;
        }
        ?></h1>
        <?php } ?>
        <form action="" method="get">
            <label for="nama">Nama</label>
            <input type="text" name="nama" id="nama">
            <label for="Nilai">Nilai</label>
            <input type="number" name="nilai" id="nilai">
            <input type="submit" value="Cek Nilai">
        </form>
    </body>
</html>