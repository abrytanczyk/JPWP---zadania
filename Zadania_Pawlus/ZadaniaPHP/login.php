<?php

// upewnij się, czy dane się zgadzają z tymi, które znajdziesz w zakładce Konta użytkowników na localhost/phpmyadmin
$servername="localhost";
$mysql_user="root";
$mysql_pass="";
$dbname="JPWP";
$conn=mysqli_connect($servername, $mysql_user, $mysql_pass, $dbname);

if($_SERVER['REQUEST_METHOD']=='POST'){
    $email=$_POST["email"];
    $password=$_POST["password"];
	$query="SELECT `name` FROM `registration` WHERE (email='$email' AND password='$password')";
	$stmt=mysqli_prepare($conn, $query);
	//mysqli_stmt_bind_param($stmt, 'ss', $email, $password);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_bind_result($stmt, $name);

    if(mysqli_stmt_fetch($stmt)){
		echo("Hello " . $name . "!");
    }else {
        echo("Error");
    }
	
}else{
echo("Error in request method");
}
?>
