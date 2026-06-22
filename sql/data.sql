-- ============================================================
-- WORK SECTIONS
-- ============================================================
INSERT INTO work_sections (type, title, hero_image, tagline) VALUES
  ('cs',        'Computer Science',  'assets/hero-ux.png',         'Building digital products through code, design, and collaboration.'),
  ('design',    'Product Design',    'assets/hero-design.png',     'Designing digital experiences through research, strategy, and iterative problem solving.'),
  ('animation', 'Animation',         'assets/hero-animation.png',  'Creating engaging stories through motion, illustration, and visual communication.'),
  ('media',     'Media',             'assets/hero-photovideo.png', 'Capturing moments through photo and video.');

-- ============================================================
-- SKILLS (sectionid matches insert order above: cs=1, design=2, etc.)
-- ============================================================
INSERT INTO section_skills (sectionid, skill) VALUES
  (1, 'React'), (1, 'TypeScript'), (1, 'JavaScript'), (1, 'Next.js'), (1, 'HTML/CSS'), (1, 'Python'), (1, 'Flask'), (1, 'SQLite'),
  (1, 'C++'), (1, 'Git'),
  (2, 'Figma'), (2, 'Wireframing'), (2, 'Prototyping'), (2, 'User Research'), ( 2, 'Adobe Creative Suite'),
  (3, 'After Effects'), (3, 'Illustrator'), (3, 'Photoshop'), (3, 'Premiere Pro'), (3, 'Blender'), (3, 'Procreate Dreams'),
  (4, 'Premiere Pro'), (4, 'Lightroom'), (4, 'Photoshop'), (4, 'After Effects');

-- ============================================================
-- CS PROJECTS
-- ============================================================
INSERT INTO cs_projects (title, start_date, end_date, featured_image, description, github_url, live_url, demo_video, display_order) VALUES
  ('MedChecker',
   'January 2025', 'April 2025',
   'uploads/cs/medchecker/MedChecker_Icon.png',
   'A web app that checks drug interactions and provides health information using AI.',
   NULL,
   NULL,
   'https://www.youtube.com/embed/277YGRorZEk?si=Jh28B_xMRunSyq9l',
   1),

  ('FANUC Internship',
   'May 2025', 'August 2025',
   'uploads/public/IMG_9002.png',
   'Designed and developed a scalable Learning Paths feature for FANUC’s training platform, enabling structured robotics training through reusable content architecture and guided technical learning experiences.',
   NULL,
   NULL,
   NULL,
   2),

  ('AI Chef',
   'May 2026', 'June 2026',
   'uploads/cs/aichef/chef-default-screen.png',
   'A React web application that generates recipes from user-provided ingredients using AI-powered text generation.',
   'https://github.com/eve1ne/ai-recipe-generator',
   NULL,
   NULL,
   3),

  ('Cat Cards',
   'December 2025', 'Present',
   'uploads/cs/catcards/cclogo.png',
   'A full-stack study app with a pixel cat companion.',
   'https://github.com/eve1ne/cat-cards',
   NULL,
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
   'MedChecker is a mobile application designed to help parents safely administer medication to children under six years old. As part of a multidisciplinary team, I contributed to the frontend experience by helping design an intuitive interface that allows caregivers to quickly access dosage guidance, medication information, and safety warnings. The goal was to reduce confusion caused by unclear medication labels and make critical health information easier to understand.',
   'Designing for healthcare-related information required balancing simplicity with accuracy. Parents often need answers quickly, so we focused on reducing cognitive load while presenting important dosage and safety details. Through iterative design reviews and usability testing, we refined navigation, information hierarchy, and task flows to ensure users could efficiently find the information they needed.',
   'The final prototype successfully demonstrated a streamlined medication guidance experience tailored to caregivers. By prioritizing accessibility, clear communication, and intuitive interactions, the application addressed a common pain point faced by parents when administering medication to young children.',
   'Flutter, Figma, Firebase, GitHub');

-- MedChecker backend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (1, 'backend',
   'MedChecker provides personalized medication guidance through weight-based dosage calculations and medication safety information. The application architecture was designed to support dosage recommendations, medication lookups, safety warnings, and future AI-assisted health features while maintaining a reliable and scalable foundation.',
   'One of the primary technical challenges was designing a system capable of providing accurate pediatric dosage recommendations while accounting for varying child weights and medication requirements. The project also required researching regulatory guidelines and pediatric medication safety standards to ensure recommendations aligned with established healthcare practices.',
   'The resulting system design supports medication information retrieval, dosage calculation logic based on Clark''s Rule, and extensibility for future features such as symptom-based recommendations and barcode scanning. The project provided valuable experience working with healthcare-related requirements, data modeling, and safety-focused application design.',
   'Firebase, Database Design, Clark''s Rule Dosage Calculations');

-- MedChecker design
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools, wireframe_image) VALUES
  (1, 'design',
   'I contributed to the UX and product design of MedChecker by helping research user needs, define requirements, and create interface concepts for parents and caregivers. Our team focused on understanding the challenges caregivers face when interpreting medication instructions and identifying opportunities to reduce medication-related errors through thoughtful design.',
   'Healthcare applications require a high degree of trust and clarity. A key challenge was translating complex medication information into a format that felt approachable and easy to understand for users with varying levels of health literacy. We conducted competitor analysis, reviewed pediatric medication safety research, and iterated on interface concepts to improve usability.',
   'The design process resulted in a user-centered prototype that emphasized safety, clarity, and efficiency. Through research-driven design decisions and iterative refinement, we created an experience that helps caregivers make more informed medication decisions while reducing uncertainty and confusion.',
   'Figma, User Research, Competitor Analysis, Usability Testing',
   'uploads/cs/medchecker/medchecker-wireframes.jpeg');

-- FANUC frontend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (2, 'frontend',
  NULL, NULL, NULL,
   'Tailwind CSS, Alpine.js, Twig, Craft CMS');

-- FANUC design
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (2, 'design',
    NULL, NULL, NULL,
   'Craft CMS, Information Architecture, UX Design, Content Modeling');

-- AI Chef frontend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools, app_image) VALUES
  (3, 'frontend',
   'AI Chef is a React-based web application that generates recipe suggestions from user-provided ingredients using a large language model. Built as part of the Scrimba Learn React curriculum, the project provided hands-on experience working with modern React development patterns, component-based architecture, state management, and API integration.',
   'One of the primary challenges was managing user input and application state while creating a smooth workflow from ingredient collection to recipe generation. The project required coordinating asynchronous API requests, conditionally rendering content based on application state, and ensuring generated recipes were presented in a clear and user-friendly format.',
   'The completed application allows users to enter available ingredients and receive AI-generated recipe recommendations in real time. Through the project, I strengthened my understanding of React hooks, component composition, API consumption, and building interactive user interfaces that incorporate AI-powered functionality.',
   'React, JavaScript, HuggingFace AI API, HTML, CSS',
   'uploads/cs/aichef/chef-generated.png');

-- Cat Cards frontend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (4, 'frontend',
   'Cat Cards is a full-stack study platform designed to help students organize course materials and generate AI-powered study resources. I built the frontend using Next.js, React, TypeScript, and Tailwind CSS, creating an interface that allows users to manage folders, upload documents, and navigate study content through a persistent learning workspace.',
   'One challenge was designing the application architecture to support future AI features while maintaining a responsive user experience. To address this, I separated long-running document processing tasks from the user interface using Trigger.dev background jobs and designed reusable frontend components that can support future study workflows.',
   'The project currently supports authentication, folder organization, PDF uploads, and document processing infrastructure. By establishing a scalable foundation early, the platform is prepared for future features such as automatic flashcard generation, AI study guides, concept summaries, and personalized learning recommendations.',
   'Next.js, React, TypeScript, Tailwind CSS, Supabase, PostgreSQL');

-- Cat Cards backend
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools) VALUES
  (4, 'backend',
   'I developed the backend infrastructure for Cat Cards using Supabase, PostgreSQL, PDF.js, and Trigger.dev. The system manages user authentication, file storage, document processing, and persistent retrieval of study materials.',
   'Processing uploaded PDFs required handling asynchronous workflows without blocking the user interface. I implemented a background processing pipeline that stores files in Supabase Storage, triggers processing jobs through Trigger.dev, extracts document text with PDF.js, and prepares content for future AI-powered analysis.',
   'The resulting architecture provides a scalable foundation for AI-powered educational tools while keeping the application responsive. The backend supports secure user data management, document storage, and automated processing workflows that can scale as new features are added.',
   'Supabase, PostgreSQL, Trigger.dev, PDF.js');

-- Cat Cards design
INSERT INTO cs_project_sections (projectid, role, overview, challenges, outcome, tools, figma_url) VALUES
  (4, 'design',
   'I designed the user experience and information architecture for Cat Cards, an AI-powered study platform that helps students organize course materials and generate study resources from uploaded documents. The design process focused on creating a workspace where users could manage multiple courses, upload study materials, and eventually interact with AI-generated learning content in a structured and intuitive way.',
   'One of the primary challenges was designing for features that had not yet been fully implemented. I needed to create an interface that supported current functionality such as folder organization, authentication, and document uploads while remaining flexible enough to accommodate future features including flashcard generation, study guides, concept summaries, and personalized learning recommendations. This required careful planning of navigation patterns, content hierarchy, and user workflows to avoid future redesigns.',
   'The resulting design establishes a scalable foundation for an AI-powered learning platform. By prioritizing organization, clarity, and long-term extensibility, Cat Cards provides students with a structured environment for managing educational content while supporting future AI-driven study experiences.',
   'Figma, Information Architecture, Wireframing, User Experience Design',
   'https://embed.figma.com/design/IbLJJpoZk9B7SVcpr1ynEr/Cat-Cards-Mock-up?node-id=0-1&embed-host=share');

-- ============================================================
-- HIGHLIGHTS
-- (sectionid matches insert order of cs_project_sections above)
-- MedChecker frontend=1, backend=2, design=3
-- FANUC frontend=4, design=5
-- AI Chef frontend=6
-- Cat Cards frontend=7, backend=8, design=9
-- ============================================================
INSERT INTO cs_section_highlights (sectionid, highlight, display_order) VALUES
  (1, 'Designed caregiver-focused interfaces that prioritized readability and accessibility', 1),
  (1, 'Created user flows for dosage lookup, medication guidance, and safety information', 2),
  (2, 'Researched and implemented dosage calculation logic based on Clark''s Rule', 1),
  (2, 'Designed a system architecture capable of supporting medication safety checks and future AI features', 2),
  (3, 'Conducted competitor analysis of existing medication guidance tools and healthcare applications', 1),
  (3, 'Defined user requirements and success metrics based on caregiver needs and medication safety concerns', 2),

  (4, 'Built reusable Twig and Tailwind components for structured learning experiences', 1),
  (4, 'Implemented dynamic routing, breadcrumbs, and learning path navigation systems', 2),
  (4, 'Designed frontend architecture to support future nested modules and certification pathways', 3),
  (5, 'Created a scalable content model for learning paths, modules, and technical training videos', 1),
  (5, 'Improved the CMS authoring experience for non-technical content managers', 2),
  (5, 'Balanced current project requirements with long-term platform scalability and maintainability', 3),

  (6, 'Implemented React state management using hooks to handle ingredient lists and recipe generation', 1),
  (6, 'Integrated an AI-powered API to generate recipes from user-provided ingredients', 2),
  (6, 'Built reusable React components and conditional rendering patterns for dynamic content display', 3),

  (7, 'Created a scalable study platform interface that supports document organization and future AI-powered learning workflows', 1),
  (7, 'Built reusable React and TypeScript components to streamline navigation and content management', 2),
  (7, 'Designed responsive user experiences optimized for managing large collections of study materials', 3),

  (7, 'Created a scalable study platform interface that supports document organization and future AI-powered learning workflows', 1),
  (7, 'Built reusable React and TypeScript components to streamline navigation and content management', 2),
  (7, 'Designed responsive user experiences optimized for managing large collections of study materials', 3),

  (9, 'Designed the platform architecture to support future AI-generated flashcards, study guides, and learning recommendations', 1),
  (9, 'Developed user flows that streamline the process of organizing and interacting with educational content', 2),
  (9, 'Created a flexible design system capable of scaling as new study tools and learning experiences are introduced', 3);

-- ============================================================
-- ART PROJECTS
-- ============================================================
INSERT INTO art_projects (type, title, start_date, end_date, featured_image, description, figma_url, display_order) VALUES
  ('design', 'Camera E-Commerce Mockup',
   'October 2025', 'November 2025',
   'uploads/public/camera_home.jpg',
   'A homepage mockup for a camera e-commerce store designed in Figma.',
   'https://embed.figma.com/design/5Sb27HOXYiHzKokWWdlBCC/Camera-E-Commerce-Mockup?node-id=0-1&embed-host=share',
   1),

  ('design', 'ALEA & Co.',
   'January 2025', 'April 2025',
   'uploads/cs/ALEA&co/prototype-image.png',
   'A mobile app that helps students find the best dining options near campus by providing real-time wait times, queue management, occupancy insights, and quick access to restaurant ordering platforms.',
   'https://embed.figma.com/proto/TA0ckCPBWmDkKGDaLBkg0u/Milestone-3?node-id=1-4&viewport=108%2C226%2C0.41&scaling=scale-down&content-scaling=fixed&starting-point-node-id=1%3A7&show-proto-sidebar=1&page-id=0%3A1&embed-host=share',
   2);

INSERT INTO art_projects (type, title, start_date, end_date, featured_image, description, video_url, display_order) VALUES
  ('animation', 'Heart Animation',     'Fall 2023', NULL, 'uploads/animation/heart_featured.png',  'I created a 2D digital animation featuring two robot characters, Blue Robot Roy and Orange Robot Mel. In this short narrative, Roy is introduced as a robot missing their heart. Through expressive animation and visual storytelling, Mel compassionately offers half of their own heart to Roy, restoring what was missing. This animation explores themes of empathy and connection, using vibrant character design and color to convey emotion and the transformative power of kindness.', 
  'https://www.youtube.com/embed/yEwKkrvpljQ?si=Wi1Bw6gRitQo39ow', 1),
  ('animation', 'Box TV Animation',    'Fall 2024', NULL, 'uploads/animation/Model_Sheet.png',  'I produced a 2D digital animation that tells the story of a box TV struggling with self-worth after comparing itself to a sleek new flat screen TV. Feeling broken and left behind, the box TV finds support when a circle-shaped TV notices its distress and gently helps put its broken pieces back together. Through expressive animation and character design, this short film explores themes of self-acceptance, empathy, and the healing power of kindness.', 
  'https://www.youtube.com/embed/li3ELNgBdf8?si=NTlY5d5_j6-wXvbJ', 2),
  ('animation', 'Ruby Animation',      'January 2023', 'Present', 'uploads/animation/ruby-title-card.jpg',   'A stray cat swept into Puerto Rico’s rough tides awakens in a dreamlike world and must choose between saving an injured companion or saving itself.', 
  NULL, 3),
  ('animation', 'AAFF Trailer',        'Fall 2025', NULL, 'uploads/animation/aaff-logo.png',   'An original animated trailer created for the Ann Arbor Film Festival trailer competition. The project combined storytelling, motion design, and animation to celebrate the festival''s creative and experimental approach to independent film.', 
  'https://www.youtube.com/embed/ECQXab_NFUg?si=2KmM9sw_P8Q8T7Zi', 4),


  ('video', 'ArtsEngine MicroGrant Video', 'Fall 2024', NULL, 'uploads/media/ArtsEngine-Block-Blue.png', 'As part of a video series supported by ArtsEngine microgrant funding, I produced and edited interviews with University of Michigan students engaged in interdisciplinary creative projects. Each video highlighted a different project, focusing on the team’s creative process, the challenges they faced, and the impact of their work.
    These interviews not only showcased the diversity and innovation of student projects, but also demonstrated the vital role of ArtsEngine funding in supporting creative exploration at U-M.', 'https://www.youtube.com/embed/xGV3NgH0AiY?si=BOCh6bjkL2zCaYAr', 1),
  ('video', 'EMR Cold Brews',              'Fall 2023',   NULL, 'uploads/media/ColdBrew_Logo.png',   'Cold Brews is a video series produced by Empty Mug Records, a local label and creative collective based in Ann Arbor, Michigan.
    Cold Brews are inspired by projects like NPR’s Tiny Desk Concerts. In each session, local or student musicians from Ann Arbor are featured performing a selection of songs in a location and with a theme of their choosing. I handle the filming and editing to create high-quality, engaging music videos that showcase each artist’s unique style. The series helps artists gain recognition and gives audiences an inside look at the diverse talent within Ann Arbor’s music scene.', 
    'https://www.youtube.com/embed/aYm70-VMjYQ?si=Iu1bEbBp0A0hGhxV', 2);

  --('photo', 'Atlas Digital Club Headshots', 'Fall 2023', NULL, 'uploads/media/ColdBrew_Logo.png',  'Placeholder text for project overview.', NULL, 1),
  --('photo', 'MFPC Club Headshots',          'Fall 2023', NULL, 'uploads/media/ColdBrew_Logo.png',   'Placeholder text for project overview.', NULL, 2),
  --('photo', 'Grad Pics',                    'Spring 2024', NULL, 'uploads/media/ColdBrew_Logo.png', 'Placeholder text for project overview.', NULL, 3);

-- ============================================================
-- ART MEDIA (add image/video urls per project, PROCESS section)
-- ============================================================
INSERT INTO art_project_media (projectid, media_type, url, caption, display_order) VALUES
  --(1, 'image', 'uploads/public/camera_home.jpg', 'Homepage hero section', 1),
  --(1, 'image', 'uploads/public/camera_home.jpg', 'Product listing page',  2);
  (2, 'image', 'uploads/cs/ALEA&co/interation-wireframe.png', 
    'The goal of this project was to help students make faster and more informed dining decisions between classes by providing information about nearby restaurants, wait times, queue status, popular menu items, and ordering options. We wanted to reduce the uncertainty students often experience when deciding where to eat, especially when they have limited time between commitments.',  1),
  (2, 'image', 'uploads/cs/ALEA&co/task-list.png', 
    'Once the initial prototype was completed, we conducted think-aloud usability testing sessions. Participants were asked to complete realistic tasks while verbalizing their thoughts, expectations, and decision-making processes. Observing users interact with the prototype helped us identify areas where the interface did not match their expectations and revealed opportunities for improvement.',  2),
  (2, 'image', 'uploads/cs/ALEA&co/uft.png', 
    'Through multiple rounds of testing and refinement, the final prototype evolved into a more intuitive and user-centered experience. Each design decision was informed by direct user feedback, allowing us to improve readability, clarify information architecture, strengthen action discoverability, and create more meaningful interactions. This iterative process reinforced the importance of validating design assumptions through testing and demonstrated how small usability improvements can significantly enhance the overall user experience.',  3),
  (2, 'video', 'https://www.youtube.com/embed/tG7RIhTYWzE?si=qS-B54kQdOpZMeFi', 
    NULL,  4);

