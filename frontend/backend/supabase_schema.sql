-- CodeKriti Hackathon Platform - Supabase Database Schema
-- Run this SQL in your Supabase SQL Editor

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================================
-- TABLES
-- ============================================================================

-- Admins table
CREATE TABLE IF NOT EXISTS admins (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  username TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Judges table
CREATE TABLE IF NOT EXISTS judges (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  judge_id TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Criteria table
CREATE TABLE IF NOT EXISTS criteria (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  max_score INTEGER NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Teams table
CREATE TABLE IF NOT EXISTS teams (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  team_name TEXT UNIQUE NOT NULL,
  leader_name TEXT,
  members TEXT[],
  members_details JSONB,
  project_name TEXT,
  project_description TEXT,
  project_url TEXT,
  photo_url TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Scores table
CREATE TABLE IF NOT EXISTS scores (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  judge_id TEXT NOT NULL,
  team_name TEXT NOT NULL,
  scores JSONB NOT NULL,
  timestamp TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(judge_id, team_name)
);

-- Team config table (single row for team password)
CREATE TABLE IF NOT EXISTS team_config (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  password_hash TEXT NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Timer config table (single row for timer settings)
CREATE TABLE IF NOT EXISTS timer_config (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  end_time TIMESTAMPTZ,
  is_active BOOLEAN DEFAULT FALSE,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================================
-- INDEXES
-- ============================================================================

CREATE INDEX IF NOT EXISTS idx_scores_team_name ON scores(team_name);
CREATE INDEX IF NOT EXISTS idx_scores_judge_id ON scores(judge_id);
CREATE INDEX IF NOT EXISTS idx_teams_team_name ON teams(team_name);
CREATE INDEX IF NOT EXISTS idx_judges_judge_id ON judges(judge_id);

-- ============================================================================
-- FUNCTIONS & TRIGGERS
-- ============================================================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger for teams table
CREATE TRIGGER update_teams_updated_at BEFORE UPDATE ON teams
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Trigger for team_config table
CREATE TRIGGER update_team_config_updated_at BEFORE UPDATE ON team_config
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Trigger for timer_config table
CREATE TRIGGER update_timer_config_updated_at BEFORE UPDATE ON timer_config
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- ROW LEVEL SECURITY (OPTIONAL - Enable if needed)
-- ============================================================================

-- Uncomment these if you want to use Supabase RLS
-- For now, we'll handle security in the backend

-- ALTER TABLE admins ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE judges ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE criteria ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE teams ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE scores ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE team_config ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE timer_config ENABLE ROW LEVEL SECURITY;

-- ============================================================================
-- INITIAL DATA
-- ============================================================================

-- Insert default admin (password: admin123)
-- Note: You'll need to generate the actual bcrypt hash
-- This is a placeholder - the backend will create it on startup
-- INSERT INTO admins (username, password_hash) 
-- VALUES ('admin', '$2b$12$...');

COMMENT ON TABLE admins IS 'Admin users for the platform';
COMMENT ON TABLE judges IS 'Judge users who evaluate teams';
COMMENT ON TABLE criteria IS 'Evaluation criteria for judging';
COMMENT ON TABLE teams IS 'Participating teams';
COMMENT ON TABLE scores IS 'Scores submitted by judges for teams';
COMMENT ON TABLE team_config IS 'Global team password configuration';
COMMENT ON TABLE timer_config IS 'Hackathon timer configuration';
