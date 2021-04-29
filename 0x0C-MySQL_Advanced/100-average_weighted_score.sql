-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DELIMITER $$DROP PROCEDUREIF EXISTS computeaverageweightedscoreforuser;
CREATE PROCEDURE computeaverageweightedscoreforuser (in user_id int) BEGIN 
UPDATE 
  users 
SET 
  average_score = (
    SELECT 
      sum(
        corrections.score * projects.weight
      ) / sum(projects.weight) 
    FROM 
      corrections 
      INNER JOIN projects ON corrections.project_id = projects.id 
      AND corrections.user_id = user_id
  ) 
WHERE 
  id = user_id;
END$$ delimiter;
