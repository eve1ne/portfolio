-- Portfolio Redesign 2026 - new tables for projects and categories

CREATE TABLE work_sections (
  sectionid INTEGER PRIMARY KEY,
  type TEXT NOT NULL,        -- 'cs', 'design', 'animation', 'media'
  title TEXT,                -- "Computer Science"
  hero_image TEXT,
  tagline TEXT
);

CREATE TABLE section_skills (
  skillid INTEGER PRIMARY KEY,
  sectionid INTEGER,
  skill TEXT,                -- "React", "Figma", "Python"
  FOREIGN KEY (sectionid) REFERENCES work_sections(sectionid)
);

CREATE TABLE cs_projects (
  projectid INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  start_date TEXT,
  end_date TEXT,
  featured_image TEXT,
  description TEXT,
  github_url TEXT,
  live_url TEXT,
  demo_video TEXT,
  is_visible INTEGER DEFAULT 1,
  display_order INTEGER DEFAULT 0
);

-- one row per role this project has
CREATE TABLE cs_project_roles (
  roleid INTEGER PRIMARY KEY,
  projectid INTEGER,
  role TEXT,                 -- 'frontend', 'backend', 'design'
  display_order INTEGER,     -- controls tab order
  FOREIGN KEY (projectid) REFERENCES cs_projects(projectid)
);

CREATE TABLE cs_project_sections (
  sectionid INTEGER PRIMARY KEY,
  projectid INTEGER,
  role TEXT,                 -- 'frontend', 'backend', 'design'
  overview TEXT,
  challenges TEXT,
  outcome TEXT,
  tools TEXT,                -- "React, Flask, SQLite"
  FOREIGN KEY (projectid) REFERENCES cs_projects(projectid)
);

-- bullet points per section (technical highlights)
CREATE TABLE cs_section_highlights (
  highlightid INTEGER PRIMARY KEY,
  sectionid INTEGER,
  highlight TEXT,
  display_order INTEGER,
  FOREIGN KEY (sectionid) REFERENCES cs_project_sections(sectionid)
);

CREATE TABLE art_projects (
  projectid INTEGER PRIMARY KEY,
  type TEXT NOT NULL,        -- 'design', 'animation', 'video', 'photo'
  title TEXT NOT NULL,
  start_date TEXT,
  end_date TEXT,
  featured_image TEXT,
  description TEXT,
  video_url TEXT,            -- YouTube/Vimeo embed
  figma_url TEXT,             -- for design projects
  is_visible INTEGER DEFAULT 1,
  display_order INTEGER DEFAULT 0
);

CREATE TABLE art_project_media (
  mediaid INTEGER PRIMARY KEY,
  projectid INTEGER,
  media_type TEXT,           -- 'image', 'video'
  url TEXT,
  caption TEXT,
  display_order INTEGER,
  FOREIGN KEY (projectid) REFERENCES art_projects(projectid)
);

CREATE TABLE certifications (
  certid INTEGER PRIMARY KEY,
  sectionid INTEGER,
  title TEXT,
  issuer TEXT,
  date TEXT,
  url TEXT,
  FOREIGN KEY (sectionid) REFERENCES work_sections(sectionid)
);
