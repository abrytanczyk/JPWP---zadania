<?php

// upewnij się, czy dane się zgadzają z tymi, które znajdziesz w zakładce Konta użytkowników na localhost/phpmyadmin
$servername="localhost";
$mysql_user="root";
$mysql_pass="";
$dbname="JPWP";
$conn=mysqli_connect($servername, $mysql_user, $mysql_pass, $dbname);

if($_SERVER['REQUEST_METHOD']=='POST'){
    $name=$_POST["name"];
    $surname=$_POST["surname"];
    $email=$_POST["email"];
    $password1=$_POST["password1"];
    $password2=$_POST["password2"];
    //done - TODO
    $name_regexp="/^[A-Z][a-z]+(\ [A-Z][a-z]+)*$/";
    $name_check = preg_match($name_regexp, $name);
    //done - TODO
    $surname_regexp="/^[A-Z][a-z]+(\-[A-Z][a-z]+)*$/";
    $surname_check = preg_match($surname_regexp, $surname);
    //done - TODO
    $email_regexp="/^[a-z\d]+[\w\d.-]*@(?:[a-z\d]+\.)+[a-z]+$/i";
    $email_check = preg_match($email_regexp, $email);
    
    //done - TODO odpowiednio sprawdź czy hasła się zgadzają
    if(($name_check == true) && ($surname_check == true) && ($email_check == true)){
		if ($password1 == $password2){
			$query="INSERT INTO `registration`(`name`, `surname`, `email`, `password`) VALUES (?,?,?,?)";
			$stmt = mysqli_prepare($conn, $query);
			mysqli_stmt_bind_param($stmt, 'ssss', $name, $surname, $email, $password1);
			mysqli_stmt_execute($stmt);

			if(mysqli_stmt_affected_rows($stmt) == 1) {
				echo("registered successfully");
			}else{
				echo("Error in registration");
			}
		} else {
			echo("Different passwords, check it and try again");
		} 
    } else {
        echo("Illegal expressions have been used");
    }

}else{
echo("Error in request method");
}
?>
