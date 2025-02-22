CREATE TABLE IF NOT EXISTS "T_THIRD_PARTY" (
    c_id SERIAL PRIMARY KEY,
    c_third_party_id VARCHAR(50) UNIQUE NOT NULL,
    c_first_name VARCHAR(100) NOT NULL,
    c_last_name VARCHAR(100) NOT NULL,
    c_national_id VARCHAR(20) NOT NULL,
    c_phone_number VARCHAR(20) NOT NULL,
    c_birth_date DATE NOT NULL,
    c_amount FLOAT NOT NULL,
    c_number_of_repayments INTEGER NOT NULL
);

-- Add any indexes
CREATE INDEX IF NOT EXISTS idx_third_party_id ON "T_THIRD_PARTY" (c_third_party_id); 