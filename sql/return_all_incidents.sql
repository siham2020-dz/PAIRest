-- Selectionner tous les incidents avec un vehicule 
-- Retourne incident_id, incident_desc et etat
SELECT "incident_id", "incident_desc", "etat"
FROM "incident"
LEFT JOIN "ordre" ON "incident"."ordre" = "ordre"."ordre_id"
WHERE "vehicule" = ?;