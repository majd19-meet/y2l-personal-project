<?php
if(!isset($_POST['submit']))
{
	echo "error;you need to submit the form";
}

$name= $_POST['name'];
$visitor_email= $_POST['email'];
$message= $_POST['message'];

if (empty($name))||empty($visitor_email))
{
	echo "Name and Email are mandatory!";
	exit;
}

$email_form= 'majdnasrawi2002@gmail.com';
$email_subject= "New form submission";
$email_body="You have received a new message from the user $name.\n"."email address: $visitor_email\n"."Here is the message:\n $message".

$to = "majdnasrawi2002@gmail.com";
$headers = "From: $email_from \r\n";

mail($to,$email_subject,$email_body,$headers);
