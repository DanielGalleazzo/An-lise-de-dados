-- Liste os 10 primeiros registros da tabela artists.

--select top 10 *
--from artists_stage

--Liste todos os artistas do Brasil.

--select *
--from artists_stage
--where country = 'Brasil'


--Mostre nome, país e gênero apenas dos artistas ativos (is_active = 1).
	--select artist_name, country, main_genre
	--from artists_stage
	--where is_active = 'True'
	
--Liste os artistas com mais de 10 milhões de ouvintes mensais.

 --select *
 --from artists_stage
 --where monthly_listeners > 10000000
 --order by  monthly_listeners

--Liste os artistas que estrearam depois de 2015.
--select *
--from artists_stage
--where debut_year > 2015
--order by debut_year

--Mostre a quantidade de artistas por país.
--select country,count(country)
--from artists_stage
--group by country

--Calcule a média de ouvintes mensais por gênero musical.
--select main_genre,AVG(monthly_listeners) AS avg_listeners
--from artists_stage
--group by main_genre


--Mostre o total de álbuns lançados por gravadora.
--select record_label, count(record_label) as total
--from artists_stage
--group by record_label

--Mostre a quantidade de artistas ativos e inativos. 
--select country, count(is_active) as true, COUNT(is_active) as false
--from artists_stage
--where is_active = 'True'
--group by country
--Descubra qual país tem mais artistas ativos.
--select country, COUNT(artist_name) as name
--from artists_stage
--where is_active = 'True'
--group by country
--Liste os 10 artistas com mais ouvintes mensais (ranking).
--select top 10 *
--from artists_stage
--order by  monthly_listeners desc
--Liste os 5 artistas com mais Grammys.
--select top 5 *
--from artists_stage
--order by  grammy_wins desc

--Mostre os 3 gêneros com maior média de ouvintes.
--Liste as gravadoras ordenadas pela soma total de ouvintes.
--Liste artistas brasileiros de Pop ou MPB com mais de 1 milhão de ouvintes.
--Liste artistas ativos com mais de 5 álbuns e pelo menos 1 Grammy.
--Liste artistas que nunca ganharam Grammy.
--Liste artistas ativos, com menos de 5 anos de carreira e mais de 500 mil ouvintes.
--Mostre quais gêneros têm mais artistas que estrearam depois de 2020.
--Calcule a “qualidade” de cada país: total de ouvintes ÷ total de artistas
--Para cada gênero, mostre: total de artistas, total de ouvintes, média de ouvintes e ranking por audiência.
--Mostre o top 3 artistas mais ouvidos de cada país.
--Para cada gravadora, mostre o artista mais popular.
--Classifique os artistas em: Superstar, Estrela ou Revelação com base nos ouvintes.


