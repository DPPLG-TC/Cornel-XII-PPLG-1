<?php

$db = new mysqli("localhost", "admin", "admin123", "sekolah");

if ($db->connect_error) {
    die("Koneksi gagal: " . $db->connect_error);
}

?>