<?php
include "db.php";
$query = $db->query("SELECT * FROM belajar");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Pelajaran</title>
    <style>
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Data Pelajaran</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nama Pelajaran</th>
                <th>Guru</th>
                <th>Hari</th>
            </tr>
        </thead>
        <tbody>
            <?php while ($row = $query->fetch_assoc()): ?>
                <tr>
                    <td><?= htmlspecialchars($row['id']) ?></td>
                    <td><?= htmlspecialchars($row['nama_pelajaran']) ?></td>
                    <td><?= htmlspecialchars($row['guru']) ?></td>
                    <td><?= htmlspecialchars($row['hari']) ?></td>
                </tr>
            <?php endwhile; ?>
        </tbody>
    </table>
</body>
</html>
