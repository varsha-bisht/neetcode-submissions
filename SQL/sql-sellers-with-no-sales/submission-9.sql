-- SELECT s.seller_name
-- FROM seller s
-- WHERE NOT EXISTS (
--   SELECT 1
--   FROM orders o
--   WHERE o.sale_date >= '2020-01-01' AND o.sale_date <= '2020-12-31' AND o.seller_id = s.seller_id
-- )
-- ORDER BY s.seller_name;

SELECT s.seller_name
FROM seller s
WHERE s.seller_id NOT IN(
  SELECT o.seller_id
  FROM orders o
  WHERE o.sale_date >= '2020-01-01' AND o.sale_date <= '2020-12-31'
)
ORDER BY s.seller_name;
