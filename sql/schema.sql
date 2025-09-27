PRAGMA foreign_keys = ON;

-- projects table
CREATE TABLE projects (
  projectid INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  image_url TEXT,        -- screenshot or thumbnail
  repo_url TEXT,         -- GitHub link
  doc_url TEXT,          -- Documentation of project 
  demo_url TEXT,         -- live demo link (optional)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- artwork pieces
CREATE TABLE artworks (
  artid INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT,
  image_url1 TEXT,
  image_url2 TEXT,
  image_url3 TEXT,
  video_url1 TEXT,           -- link to animation or video project
  video_url2 TEXT,
  video_url3 TEXT,
  medium TEXT NOT NULL,              -- e.g., "Digital", "Videography"
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
