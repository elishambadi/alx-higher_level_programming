-- Select and list all California Cities
SELECT id, name FROM cities WHERE state_id=(
   SELECT s.id FROM states s WHERE name='California');
