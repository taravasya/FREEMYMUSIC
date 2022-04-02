<?php
    require_once 'private_cfg.php';
    $spotify_data = [
        $data = array (
            'client_id'     => $private_data['spotify']['client_id'],
            'client_secret' => $private_data['spotify']['client_secret'],
            'redirect_uri'  => 'http://oauth.local/callback.php',
            'scope'         => 'user-read-private user-read-email',
            'response_type' => 'code'
        ),
        'oauth_url'         => 'https://accounts.spotify.com/authorize?' . http_build_query($data),
        'enable'            => 1,
        'export'            => ['enabled' => 1, ['list' => ['artists', 'albums', 'playlists']]],
        'import'            => ['enabled' => 0, ['list' => ['artists', 'albums', 'playlists']]],
        'name'              => 'Spotify'
    ]
?>