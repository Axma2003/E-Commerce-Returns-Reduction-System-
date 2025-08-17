-- Identify top 5 reasons for product returns
SELECT return_reason, COUNT(*) AS return_count
FROM customer_returns
GROUP BY return_reason
ORDER BY return_count DESC
LIMIT 5;

-- Join reviews with returns to analyze correlation
SELECT r.product_id, r.review_text, c.return_reason
FROM product_reviews r
JOIN customer_returns c
ON r.product_id = c.product_id;
