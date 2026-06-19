-- ============================================================
-- WORK SECTIONS
-- ============================================================
INSERT INTO work_sections (type, title, hero_image, tagline) VALUES
  ('cs',        'Computer Science',  'assets/hero-ux.png',         'Building things that work.'),
  ('design',    'Product Design',    'assets/hero-design.png',     'Designing things that feel right.'),
  ('animation', 'Animation',         'assets/hero-animation.png',  'Bringing ideas to life.'),
  ('media',     'Media',             'assets/hero-photovideo.png', 'Capturing moments.');

-- ============================================================
-- SKILLS (sectionid matches insert order above: cs=1, design=2, etc.)
-- ============================================================
INSERT INTO section_skills (sectionid, skill) VALUES
  (1, 'React'), (1, 'Python'), (1, 'Flask'), (1, 'SQLite'),
  (1, 'HTML/CSS'), (1, 'JavaScript'),
  (2, 'Figma'), (2, 'Wireframing'), (2, 'Prototyping'), (2, 'User Research'),
  (3, 'After Effects'), (3, 'Illustrator'),
  (4, 'Premiere Pro'), (4, 'Lightroom'), (4, 'Photography');

-- ============================================================
-- CS PROJECTS
-- ============================================================
INSERT INTO cs_projects (title, start_date, end_date, featured_image, description, github_url, live_url, display_order) VALUES
  ('MedChecker',
   'Jan 2024', 'Apr 2024',
   'uploads/medchecker/featured.png',
   'A web app that checks drug interactions and provides health information using AI.',
   NULL,
   NULL,
   1),

  ('FANUC Learning Paths',
   'May 2024', 'Aug 2024',
   'uploads/fanuc/featured.png',
   'An internal learning management system for FANUC employees to track training progress.',
   NULL,
   NULL,
   2),

  ('AI Chef',
   'Oct 2023', 'Dec 2023',
   'uploads/ai-chef/featured.png',
   'An AI-powered recipe generator that creates recipes based on ingredients you have.',
   'https://github.com/eve1ne/ai-recipe-generator',
   NULL,
   3),

  ('Cat Cards',
   'Sep 2023', 'Oct 2023',
   'uploads/cat-cards/featured.png',
   'A full-stack flashcard app with a cat theme.',
   'https://github.com/eve1ne/cat-cards',
   NULL,
   4);

-- ============================================================
-- CS PROJECT ROLES
-- (projectid: MedChecker=1, FANUC=2, AI Chef=3, Cat Cards=4)
-- ============================================================
INSERT INTO cs_project_roles (projectid, role, display_order) VALUES
  (1, 'frontend', 1), (1, 'backend', 2), (1, 'design', 3),
  (2, 'frontend', 1), (2, 'design',   2),
  (3, 'frontend', 1),
  (4, 'frontend', 1), (4, 'backend',  2), (4, 'design', 3);

-- ============================================================
-- CS PROJECT SECTIONS
-- ============================================================

-- MedChecker frontend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (1, 'frontend',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'React, HTML, CSS, JavaScript');

-- MedChecker backend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (1, 'backend',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'Python, Flask, SQLite');

-- MedChecker design
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (1, 'design',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'Figma');

-- FANUC frontend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (2, 'frontend',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'React, CSS');

-- FANUC design
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (2, 'design',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'Figma');

-- AI Chef frontend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (3, 'frontend',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'React, JavaScript');

-- Cat Cards frontend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (4, 'frontend',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'HTML, CSS, JavaScript');

-- Cat Cards backend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (4, 'backend',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'Python, Flask, SQLite');

-- Cat Cards design
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (4, 'design',
   'Placeholder text for project overview. This should be a concise summary of the project and your role in it.',
   'Placeholder text for challenges faced during the project. This should highlight any technical or design obstacles you overcame.',
   'Placeholder text for project outcome. This should describe the impact or results of the project.',
   'Figma');

-- ============================================================
-- HIGHLIGHTS
-- (sectionid matches insert order of cs_project_sections above)
-- MedChecker frontend=1, backend=2, design=3
-- FANUC frontend=4, design=5
-- AI Chef frontend=6
-- Cat Cards frontend=7, backend=8, design=9
-- ============================================================
INSERT INTO cs_section_highlights (sectionid, highlight, display_order) VALUES
  (1, 'Built reusable accessible React components following WCAG guidelines', 1),
  (1, 'Implemented responsive layout across mobile and desktop', 2),
  (2, 'Designed normalized schema for drug interaction data', 1),
  (2, 'Built error handling for inconsistent third-party API responses', 2),
  (3, 'Conducted user interviews with 5 participants', 1),
  (3, 'Iterated through 3 rounds of wireframes before high-fidelity', 2),
  (4, 'Built modular component system reused across 8 page templates', 1),
  (6, 'Integrated OpenAI streaming API for real-time recipe output', 1),
  (6, 'Handled edge cases for missing or unusual ingredients', 2);

-- ============================================================
-- ART PROJECTS
-- ============================================================
INSERT INTO art_projects (type, title, start_date, end_date, featured_image, description, figma_url, display_order) VALUES
  ('design', 'Camera E-Commerce Mockup',
   'Feb 2024', 'Mar 2024',
   'uploads/camera/featured.png',
   'A homepage mockup for a camera e-commerce store designed in Figma.',
   'https://figma.com/your-link-here',
   1),

  ('design', 'ALEA & Co.',
   'Jan 2024', 'Apr 2024',
   'uploads/alea/featured.png',
   'Full product design case study for a startup brand identity and app.',
   'https://figma.com/your-link-here',
   2);

INSERT INTO art_projects (type, title, start_date, end_date, featured_image, description, display_order) VALUES
  ('animation', 'Heart Animation',     'Fall 2023', NULL, 'uploads/animation/heart.png',  'Placeholder text for project overview.', 1),
  ('animation', 'Box TV Animation',    'Fall 2023', NULL, 'uploads/animation/boxtv.png',  'Placeholder text for project overview.', 2),
  ('animation', 'Ruby Animation',      'Fall 2023', NULL, 'uploads/animation/ruby.png',   'Placeholder text for project overview.', 3),
  ('animation', 'Cat Walk Cycle',      'Fall 2023', NULL, 'uploads/animation/cat.png',    'Placeholder text for project overview.', 4),
  ('animation', 'AAFF Trailer',        'Fall 2023', NULL, 'uploads/animation/aaff.png',   'Placeholder text for project overview.', 5),

  ('video', 'ArtsEngine MicroGrant Video 1', 'Spring 2024', NULL, 'uploads/video/artse1.png', 'Placeholder text for project overview.', 1),
  ('video', 'ArtsEngine MicroGrant Video 2', 'Spring 2024', NULL, 'uploads/video/artse2.png', 'Placeholder text for project overview.', 2),
  ('video', 'EMR Cold Brews 1',              'Fall 2023',   NULL, 'uploads/video/emr1.png',   'Placeholder text for project overview.', 3),
  ('video', 'EMR Cold Brews 2',              'Fall 2023',   NULL, 'uploads/video/emr2.png',   'Placeholder text for project overview.', 4),
  ('video', 'EMR Cold Brews 3',              'Fall 2023',   NULL, 'uploads/video/emr3.png',   'Placeholder text for project overview.', 5),
  ('video', 'EMR Live Show',                 'Fall 2023',   NULL, 'uploads/video/emrlive.png','Placeholder text for project overview.', 6),

  ('photo', 'Atlas Digital Club Headshots', 'Fall 2023', NULL, 'uploads/photo/atlas.png',  'Placeholder text for project overview.', 1),
  ('photo', 'MFPC Club Headshots',          'Fall 2023', NULL, 'uploads/photo/mfpc.png',   'Placeholder text for project overview.', 2),
  ('photo', 'Grad Pics',                    'Spring 2024', NULL, 'uploads/photo/grad.png', 'Placeholder text for project overview.', 3);

-- ============================================================
-- ART MEDIA (add image/video urls per project as you have them)
-- ============================================================
INSERT INTO art_project_media (projectid, media_type, url, caption, display_order) VALUES
  (1, 'image', 'uploads/camera/screen1.png', 'Homepage hero section', 1),
  (1, 'image', 'uploads/camera/screen2.png', 'Product listing page',  2);
