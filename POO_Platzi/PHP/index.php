<?php

require_once('car.php');
require_once('account.php');
require_once('uberX.php');
require_once('uberPool.php');
require_once('uberBlack.php');
require_once('uberVan.php');

$uberX = new UberX("CVB123", new Account("Andres", "111"), "Chevrolet", "Spark");
$uberX->setPassenger(4);
$uberX->printDataCar();

$uberVan = new UberVan("OJL395", new Account("JP", "AND456"), "Nissan", "Versa");
$uberVan->setPassenger(6);
$uberVan->printDataCar();

?>