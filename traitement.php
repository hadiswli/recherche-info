<?php
$serveur= "localhost";
$login= "root";
$pass= "";
$database= "ecole";
$connexion = mysqli_connect($serveur, $login, $pass, $database);
if (!$connexion) {
    die("Connection failed: " . mysqli_connect_error());
}
else {
    if (isset($_POST['name']) && isset($_POST['prenom']) && isset($_POST['classe']) && isset($_POST['email']) && isset($_POST['tel']) && isset($_POST['matricule'])) {
        $name = $_POST['name'];
        $prenom = $_POST['prenom'];
        $classe = $_POST['classe'];
        $email = $_POST['email'];
        $tel = $_POST['tel'];
        $matricule = $_POST['matricule'];
        $sql = "INSERT INTO etudiant (nom, prenom, classe, email, tel, matricule) VALUES ('$name', '$prenom', '$classe', '$email', '$tel', '$matricule')";
        if (mysqli_query($connexion, $sql)) {
            header("Location: index.php?key=ok");
            exit();
        } else {
            header("Location: index.php?key=no");
            exit();
        }
    }
    mysqli_close($connexion);
}
?>
