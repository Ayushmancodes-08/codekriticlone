"""
Supabase client wrapper for CodeKriti Hackathon Platform
Provides helper functions for database operations
"""
import os
from supabase import create_client, Client
from typing import Optional, List, Dict, Any

# Initialize Supabase client
supabase_url = os.environ.get('SUPABASE_URL')
supabase_key = os.environ.get('SUPABASE_SERVICE_KEY')

if not supabase_url or not supabase_key:
    raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in environment variables")

supabase: Client = create_client(supabase_url, supabase_key)


class SupabaseDB:
    """Helper class for Supabase database operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    # ============================================================================
    # ADMINS
    # ============================================================================
    
    async def find_admin(self, username: str) -> Optional[Dict]:
        """Find admin by username"""
        response = self.client.table('admins').select('*').eq('username', username).execute()
        return response.data[0] if response.data else None
    
    async def create_admin(self, username: str, password_hash: str) -> Dict:
        """Create a new admin"""
        response = self.client.table('admins').insert({
            'username': username,
            'password_hash': password_hash
        }).execute()
        return response.data[0]
    
    # ============================================================================
    # JUDGES
    # ============================================================================
    
    async def find_judge(self, judge_id: str) -> Optional[Dict]:
        """Find judge by judge_id"""
        response = self.client.table('judges').select('*').eq('judge_id', judge_id).execute()
        return response.data[0] if response.data else None
    
    async def create_judge(self, judge_id: str, name: str, password_hash: str) -> Dict:
        """Create a new judge"""
        response = self.client.table('judges').insert({
            'judge_id': judge_id,
            'name': name,
            'password_hash': password_hash
        }).execute()
        return response.data[0]
    
    async def get_all_judges(self) -> List[Dict]:
        """Get all judges (excluding password_hash)"""
        response = self.client.table('judges').select('id, judge_id, name, created_at').execute()
        return response.data
    
    # ============================================================================
    # CRITERIA
    # ============================================================================
    
    async def create_criteria(self, criteria_id: str, name: str, max_score: int) -> Dict:
        """Create evaluation criteria"""
        response = self.client.table('criteria').insert({
            'id': criteria_id,
            'name': name,
            'max_score': max_score
        }).execute()
        return response.data[0]
    
    async def get_all_criteria(self) -> List[Dict]:
        """Get all criteria"""
        response = self.client.table('criteria').select('*').execute()
        return response.data
    
    async def delete_criteria(self, criteria_id: str) -> int:
        """Delete criteria by ID"""
        response = self.client.table('criteria').delete().eq('id', criteria_id).execute()
        return len(response.data)
    
    # ============================================================================
    # TEAMS
    # ============================================================================
    
    async def find_team(self, team_name: str) -> Optional[Dict]:
        """Find team by team_name"""
        response = self.client.table('teams').select('*').eq('team_name', team_name).execute()
        return response.data[0] if response.data else None
    
    async def create_team(self, team_name: str) -> Dict:
        """Create a new team"""
        response = self.client.table('teams').insert({
            'team_name': team_name
        }).execute()
        return response.data[0]
    
    async def update_team(self, team_name: str, data: Dict) -> Dict:
        """Update team profile"""
        response = self.client.table('teams').update(data).eq('team_name', team_name).execute()
        return response.data[0] if response.data else None
    
    async def get_all_teams(self) -> List[Dict]:
        """Get all teams"""
        response = self.client.table('teams').select('*').execute()
        return response.data
    
    # ============================================================================
    # SCORES
    # ============================================================================
    
    async def find_score(self, judge_id: str, team_name: str) -> Optional[Dict]:
        """Find score by judge and team"""
        response = (self.client.table('scores')
                   .select('*')
                   .eq('judge_id', judge_id)
                   .eq('team_name', team_name)
                   .execute())
        return response.data[0] if response.data else None
    
    async def create_score(self, judge_id: str, team_name: str, scores: Dict, timestamp: str) -> Dict:
        """Create a new score"""
        response = self.client.table('scores').insert({
            'judge_id': judge_id,
            'team_name': team_name,
            'scores': scores,
            'timestamp': timestamp
        }).execute()
        return response.data[0]
    
    async def update_score(self, judge_id: str, team_name: str, scores: Dict, timestamp: str) -> Dict:
        """Update an existing score"""
        response = (self.client.table('scores')
                   .update({'scores': scores, 'timestamp': timestamp})
                   .eq('judge_id', judge_id)
                   .eq('team_name', team_name)
                   .execute())
        return response.data[0]
    
    async def get_team_scores(self, team_name: str) -> List[Dict]:
        """Get all scores for a team"""
        response = self.client.table('scores').select('*').eq('team_name', team_name).execute()
        return response.data
    
    # ============================================================================
    # TEAM CONFIG
    # ============================================================================
    
    async def get_team_config(self) -> Optional[Dict]:
        """Get team password configuration"""
        response = self.client.table('team_config').select('*').limit(1).execute()
        return response.data[0] if response.data else None
    
    async def set_team_config(self, password_hash: str) -> Dict:
        """Set or update team password configuration"""
        # Delete all existing configs
        self.client.table('team_config').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()
        # Insert new config
        response = self.client.table('team_config').insert({
            'password_hash': password_hash
        }).execute()
        return response.data[0]
    
    # ============================================================================
    # TIMER CONFIG
    # ============================================================================
    
    async def get_timer_config(self) -> Optional[Dict]:
        """Get timer configuration"""
        response = self.client.table('timer_config').select('*').limit(1).execute()
        return response.data[0] if response.data else None
    
    async def set_timer_config(self, end_time: str, is_active: bool) -> Dict:
        """Set or update timer configuration"""
        # Delete all existing configs
        self.client.table('timer_config').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()
        # Insert new config
        response = self.client.table('timer_config').insert({
            'end_time': end_time,
            'is_active': is_active
        }).execute()
        return response.data[0]


# Global database instance
db = SupabaseDB(supabase)
