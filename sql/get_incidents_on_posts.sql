SELECT incident.incident_id, ordre.ordre_id, poste.poste_id, poste.poste_desc
FROM incident
INNER JOIN ordre ON incident.ordre = ordre.ordre_id
INNER JOIN poste ON ordre.poste = poste.poste_id
WHERE ordre.vehicule = ?;