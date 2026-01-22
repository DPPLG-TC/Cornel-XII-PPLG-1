
<?php 
function nilai(){
    
}
// function handle isset
function cek_data($data){

    if(isset($data)){
        return $data;
    }else{
        return false;
    }

}


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LSP Pass Test</title>
</head>
<body>
    <h1><?php echo cek_data($_GET['nama']); ?></h1>
    <h1><?php echo cek_data($_GET['nilai']); ?></h1>
    <form action="" method="get">
        <label for="nama">Nama Peserta</label>
        <input type="text" name="nama" id="nama">
        <label for="nilai">Nilai LSP</label>
        <input type="number" name="nilai" id="nilai">
        <input type="submit" value="cek">
    </form>
</body>
</html>
