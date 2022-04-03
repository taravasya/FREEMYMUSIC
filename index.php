<?php
	require_once 'cfgs/cfg.php';
	require_once 'functions/helpers.php';
	debug_log($spotify_data, __LINE__, 'test.log', false);
	//ЗДЕСЬ HOOK ДЛЯ CFG $spotify_data
?>

<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
		<!-- styles -->
		<link rel="stylesheet" type="text/css" href="assets/css/fmm_style.css">
		<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Yesteryear">
		<link rel="stylesheet" type="text/css" href="assets/fonts/noun-icons/noun-webfont.css">
		<title>Free My Music!</title>
	</head>
	<body>
	<div class="fmm_meta_company"></div>
	<div class="fmm_head">
		<img class="fmm_logo" src="assets/imgs/logo.svg">
    </div>
	<div class="fmm_main">
        <div class="fmm_service_items">
			<?php
				for ($i = 1; $i <= 10; $i++) {
	                include 'layouts/service_item.php';
	            }
        	?>
		</div>
        <a href="<?php echo $spotify_data['oauth_url']; ?>">Login</a>
    </div>
	</body>
</html>