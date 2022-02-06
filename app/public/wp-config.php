<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'local' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', 'root' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'W4O/huyTu2aBeMmE7cTuf13Qr73TiChWE8eL4RdLgNkwJWZjsTdEC62hN2eVmAyEArpp011si2ED+4VEzQX1zA==');
define('SECURE_AUTH_KEY',  'l53PnJuzqDvJ/RWAc6vzbJLySPBJ8OcTVzW+uwDRIhRuHmXrrIGfjvVEGwdfLo47Yr480AyTg2jFGl7b6erpjw==');
define('LOGGED_IN_KEY',    'YTS6WAPv3HNyRJ9K8IgmAgqrQbwHzlBUbki6hYvD6OQ5IOHQHI1DAohP47oZtThuNgtlMV/3ACC71nVVtV5NmQ==');
define('NONCE_KEY',        'Ih1s4UJR8qgBXX8wMSAOyBl35hoFRX5FTRGo7AMeNp2bx1Lpjb7aLct1icelje8LAgLZBXyji37kdBNKw8N1hg==');
define('AUTH_SALT',        'UTTj5dnO8jiECi5U5dfFKRn/QqWyPwHWtBiCf/aS65OCK+NLmLZTnHCJ8954JgB96PJdFLmLfFLzxoC6bd1KhA==');
define('SECURE_AUTH_SALT', '4FahMwcvtYCt0pxRbloNiPQDhe6kGyoqzFJk2SJ4I/KeROauTFlocpFns0gPr/Dys5b6kdna2T2ClgRHmlpm3w==');
define('LOGGED_IN_SALT',   'nI/veNAJE2A6US12Ef4iU5uHkXBLF1tDNRJJy3N2Nv8UoLaaz1ph+/6/k7Sa8QfpoFwJXmeyvfC+JhgF/uxdKA==');
define('NONCE_SALT',       'IOWn+jwb8jkYjfywrABrdS8Ft26iZpEVnQi3vaQHjBWR8lLNHu5Q6w7H9/Zlcd5MtFVtbTKnctfDGpJtpMxMvg==');

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';




/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
