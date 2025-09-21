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
  image_url TEXT NOT NULL,
  video_url TEXT,           -- link to animation or video project
  medium TEXT,              -- e.g., "Digital", "Videography"
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
