PRAGMA foreign_keys = ON;

INSERT INTO projects(projectid, title, description, image_url, doc_url, demo_url, created_at)
VALUES 
    (2, 'MedChecker', 
    '
        MedChecker is a mobile app designed to help parents safely manage medication for young children under six. The app provides clear dosage guidelines using Clark’s Rule, reliable information on common medications, and a simple, intuitive interface. By addressing the lack of dosage instructions for children on most medication bottles, MedChecker reduces parental stress and lowers the risk of medication errors, especially for families with limited access to healthcare.
        
        Unlike many existing apps that require subscriptions or focus on other demographics, MedChecker prioritizes accessibility and ease of use for new parents. In the long term, the app aims to expand to other groups, such as the elderly, while maintaining up-to-date medical data and strong security practices.
    ', 
    'public/497_Logo.png', 'public/MedChecker_Documentation.pdf', 'https://www.youtube.com/embed/277YGRorZEk?si=LLlEbl4FEMqCjluF', 'January 8th 2025 - April 22nd 2025');


INSERT INTO artworks(title, description, image_url1, image_url2, image_url3, video_url1, video_url2, video_url3, medium)
VALUES 
    ('Box TV Animation', 
    '
        I produced a 2D digital animation that tells the story of a box TV struggling with self-worth after comparing itself to a sleek new flat screen TV. Feeling broken and left behind, the box TV finds support when a circle-shaped TV notices its distress and gently helps put its broken pieces back together. Through expressive animation and character design, this short film explores themes of self-acceptance, empathy, and the healing power of kindness.

    ', 
    'public/Model_Sheet.png', NULL, NULL, 'https://www.youtube.com/embed/li3ELNgBdf8?si=FMTIt0eDC7RrfFm6', NULL, NULL, '2D Animation'),
    ('Heart Animation', 
    '
        I created a 2D digital animation featuring two robot characters, Blue Robot Roy and Orange Robot Mel. In this short narrative, Roy is introduced as a robot missing their heart. Through expressive animation and visual storytelling, Mel compassionately offers half of their own heart to Roy, restoring what was missing. This animation explores themes of empathy and connection, using vibrant character design and color to convey emotion and the transformative power of kindness.

    ', 
    'public/heart_featured.png', 'public/Roy_The_Robot.png', 'public/Mel_The_Robot.png', 'https://www.youtube.com/embed/yEwKkrvpljQ?si=kpwMHzNNQ2oppPQy', NULL, NULL, '2D Animation/Digital Art'),
    ('Naptime Music Project', 
    '
        Naptime Music Project is an alternative rock band I co-founded at the University of Michigan, where I contribute vocals and electric guitar. Collaborating closely with my bandmates, we write and perform original songs at campus venues and events, emphasizing a strong sense of teamwork and creative exchange. 

        In addition to performing, I lead the visual direction of the project by designing digital artwork, logos, and merchandise that capture our group’s unique identity. This project integrates music, performance, and visual art, showcasing our combined talents both on stage and through our branding.
    ', 
    'public/Naptime_Logo_1.png', 'public/Naptime_Logo_5.png', 'public/Naptime_Sleepy.png', NULL, NULL, NULL, 'Music/Art'),
    ('Cold Brew Music Videos', 
    '
        Cold Brews is a video series produced by Empty Mug Records, a local label and creative collective based in Ann Arbor, Michigan.
        
        Cold Brews are inspired by projects like NPR’s Tiny Desk Concerts. In each session, local or student musicians from Ann Arbor are featured performing a selection of songs in a location and with a theme of their choosing. I handle the filming and editing to create high-quality, engaging music videos that showcase each artist’s unique style. The series helps artists gain recognition and gives audiences an inside look at the diverse talent within Ann Arbor’s music scene.
        
        Instagram: @emptymugrecords
    ', 
    'public/ColdBrew_Logo.png', NULL, NULL, 'https://www.youtube.com/embed/aYm70-VMjYQ?si=CKOH0bVagb1rv8vn', 'https://www.youtube.com/embed/FOi9RHJW6KY?si=6msZqoxeTSZqvSQO', 'https://www.youtube.com/embed/euMCxIPv2LQ?si=Bfdvx6Mzdqqi51vR', 'Videography/Editing'),
    ('ArtsEngine MicroGrant Videos', 
    '
        As part of a video series supported by ArtsEngine microgrant funding, I produced and edited interviews with University of Michigan students engaged in interdisciplinary creative projects. Each video highlighted a different project, focusing on the team’s creative process, the challenges they faced, and the impact of their work. 

        These interviews not only showcased the diversity and innovation of student projects, but also demonstrated the vital role of ArtsEngine funding in supporting creative exploration at U-M.
    ', 
    'public/ArtsEngine-Block-Blue.png', NULL, NULL, 'https://player.vimeo.com/video/1094160226?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479', NULL, NULL, 'Videography/Editing'),
    ('Camera E-commerce Website Mockup', 
    '
        I created a Figma mockup of a clean, modern homepage for a camera store featuring an intuitive mega menu, hero banner with strong CTA, three product categories, and four highlighted products. Includes a promo banner, SEO-focused section, and a footer with links, social media, and newsletter signup in order to deliver a seamless shopping experience.
    ', 
    'public/camera_home.jpg', NULL, NULL, 'https://embed.figma.com/proto/5Sb27HOXYiHzKokWWdlBCC/Camera-E-Commerce-Mockup?page-id=0%3A1&node-id=1-2&viewport=932%2C236%2C0.85&scaling=min-zoom&content-scaling=fixed&embed-host=share', NULL, NULL, 'Figma/Design');
