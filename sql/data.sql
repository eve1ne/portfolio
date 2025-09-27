PRAGMA foreign_keys = ON;

INSERT INTO projects(title, description, image_url, doc_url, demo_url, created_at)
VALUES 
    ('FANUC Internship', 'Designed and implemented scalable courses', 'PlaceholderImage.jpg', NULL, NULL, 'May 12th 2025 - August 8th 2025'),
    ('MedChecker', 
    'MedChecker is a mobile app designed to help parents safely manage medication for young children under six. The app provides clear dosage guidelines using 
    Clark’s Rule, reliable information on common medications, and a simple, intuitive interface. By addressing the lack of dosage instructions for children on most 
    medication bottles, MedChecker reduces parental stress and lowers the risk of medication errors, especially for families with limited access to healthcare. 
    Unlike many existing apps that require subscriptions or focus on other demographics, MedChecker prioritizes accessibility and ease of use for new parents. 
    In the long term, the app aims to expand to other groups, such as the elderly, while maintaining up-to-date medical data and strong security practices.', 
    '497_Logo.png', 'MedChecker_Documentation.pdf', 'https://www.youtube.com/embed/277YGRorZEk?si=LLlEbl4FEMqCjluF', 'January 8th 2025 - April 22nd 2025');


INSERT INTO artworks(title, description, image_url1, image_url2, image_url3, video_url1, video_url2, video_url3, medium)
VALUES 
    ('Cold Brew Music Videos', 'temp description', 'ColdBrew_Logo.png', NULL, NULL, 'https://www.youtube.com/embed/aYm70-VMjYQ?si=CKOH0bVagb1rv8vn', 'https://www.youtube.com/embed/FOi9RHJW6KY?si=6msZqoxeTSZqvSQO', 'https://www.youtube.com/embed/euMCxIPv2LQ?si=Bfdvx6Mzdqqi51vR', 'Videography/Editing'),
    ('ArtsEngine MicroGrant Videos', 'temp description', 'ColdBrew_Logo.png', NULL, NULL, 'https://player.vimeo.com/video/1094160226?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479', NULL, NULL, 'Videography/Editing'),
    ('Box TV Animation', 'temp description', 'Model_Sheet.png', NULL, NULL, 'https://www.youtube.com/embed/li3ELNgBdf8?si=FMTIt0eDC7RrfFm6', NULL, NULL, '2D Animation'),
    ('Heart Animation', 'temp description', 'heart.png', 'RoyMel_character.png', 'Project1C.gif', 'https://www.youtube.com/embed/yEwKkrvpljQ?si=kpwMHzNNQ2oppPQy', NULL, NULL, '2D Animation/Digital Art'),
    ('Digital Illustration Studies', 'temp description', 'Closet.png', 'Skeleton_Study.png', 'Hand_Study.png', NULL, NULL, NULL, 'Digital Art'),
    ('Naptime Band', 'temp description', 'Naptime_Logo_1.png', 'Naptime_Logo_5.png', 'Naptime_Sleepy.png', NULL, NULL, NULL, 'Music/Art');
