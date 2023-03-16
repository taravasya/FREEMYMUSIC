<?php
	require_once 'cfgs/cfg.php';
	require_once 'functions/helpers.php';
	debug_log($spotify_data, __LINE__, 'test.log', false);
	//ЗДЕСЬ HOOK ДЛЯ CFG $spotify_data
?>

<!DOCTYPE html>
<html lang="ru">
	<?php include 'layouts/head.php'; ?>
	<body>
		<div class="fmm_meta_company"></div>
		<?php include 'layouts/header.php'; ?>
		<?php include 'layouts/main.php'; ?>
	</body>
</html>