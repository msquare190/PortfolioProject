--Run In Bigquery

select location, max (total_deaths) as TotalDeathCount
from `portfolio-387612.covid_death.covid2`
where continent is not null
group by location
order by TotalDeathCount desc 

--Breaking Things Down By Continent

select continent, max (total_deaths) as TotalDeathCount
from `portfolio-387612.covid_death.covid2`
where continent is not null
group by continent
order by TotalDeathCount desc 


--Showing the continent with the highest death count per population

select continent, max (total_deaths) as TotalDeathCount
from `portfolio-387612.covid_death.covid2`
where continent is not null
group by continent
order by TotalDeathCount desc 

select *
from `portfolio-387612.covid_death.covid2`
where continent is not null
order by 3,4


--Global Numbers

select sum(new_cases) as total_cases, sum(new_deaths) as total_deaths, 
sum(new_deaths)/sum(new_cases)*100 as DeathPercentage
from `portfolio-387612.covid_death.covid2`
where continent is not null
--GROUP BY date
order by 1,2


--Loking at Total Population vs Vaccination (total no. of people in the world that has been vaccinated)


select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(vac.new_vaccinations) OVER (partition by dea.location order by dea.location,
dea.date) as Rollingpeoplevaccinated
-- (Rollingpeoplevaccinated/population)*100
from `portfolio-387612.covid_death.covid2` dea
join `portfolio-387612.covid_vaccination.covid` vac
on dea.location = vac.location
and dea.date = vac.date
order by 2,3


----Use CTE

With popvsvac as 
(
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(vac.new_vaccinations) OVER (partition by dea.location order by dea.location,
dea.date) as Rollingpeoplevaccinated
-- (Rollingpeoplevaccinated/population)*100
from `portfolio-387612.covid_death.covid2` dea
join `portfolio-387612.covid_vaccination.covid` vac
on dea.location = vac.location
and dea.date = vac.date
--order by 2,3
)
select *, (Rollingpeoplevaccinated/population)*100
from popvsvac 


--Temp Table


CREATE Temporary Table percentpopulationvaccinated
(
  continent string,
  location string,
  date date,
  population numeric,
  new_vaccinations numeric,
  Rollingpeoplevaccinated numeric
);
Insert into percentpopulationvaccinated
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(vac.new_vaccinations) OVER (partition by dea.location order by dea.location,
dea.date) as Rollingpeoplevaccinated
/*(Rollingpeoplevaccinated/population)*100 */
from `portfolio-387612.covid_death.covid2` dea
join `portfolio-387612.covid_vaccination.covid` vac
on dea.location = vac.location
and dea.date = vac.date;
/* order by 2,3 */
select *, (Rollingpeoplevaccinated / population)*100
from  percentpopulationvaccinated;

/* Creating View to Store for Data Visualization*/

SELECT *
FROM `portfolio-387612._scripta5bf432a20acc3ac362112c44e2dfcd0e1d52d17.percentpopulationvaccinated` 

