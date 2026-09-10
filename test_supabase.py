from database.supabase_client import supabase

response = supabase.table("scan_history").select("*").limit(1).execute()

print("Supabase connected successfully!")
print(response.data)