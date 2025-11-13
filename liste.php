<?php 
$serveur= "localhost";
$login= "root";
$pass= "";
$database= "ecole";
$connexion = mysqli_connect($serveur, $login, $pass, $database);
if (!$connexion) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
    $sql = "SELECT * FROM etudiant";
    $result = mysqli_query($connexion, $sql);
    if (mysqli_num_rows($result) == 0) {
       echo "aucun enregistrement trouvé"; 
    } else {?>
        <table border="1" style="width:100%"> 

         <tr>
              <th>Nom</th>
              <th>Prenom</th>
              <th>Classe</th>
              <th>Email</th>
              <th>Tel</th>
              <th>Matricule</th>
         </tr>
         <?php 
         while($row = mysqli_fetch_assoc($result)) { ?>
            
         <tr>
                <td><?php echo $row['nom']; ?></td>
                <td><?php echo $row['prenom']; ?></td>
                <td><?php echo $row['classe']; ?></td>
                <td><?php echo $row['email']; ?></td>
                <td><?php echo $row['tel']; ?></td>
                <td><?php echo $row['matricule']; ?></td>
         </tr>
        
         <?php } 
         ?>
        
   </table>

   <?php }
    ?>
   
</body>
</html>
