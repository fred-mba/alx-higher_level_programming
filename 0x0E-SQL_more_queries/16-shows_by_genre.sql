-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked

SELECT
	tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN
	tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN
	tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY
	tv_shows.title, tv_genres.name;