async function getAchievements() {
  const lodestoneLink = document.getElementById("lodestone-link").value;
  const lodestoneIdMatch = lodestoneLink.match(/lodestone\/character\/(\d+)/);
  
  if (!lodestoneIdMatch) {
    alert("Invalid Lodestone profile link");
    return;
  }

  const lodestoneId = lodestoneIdMatch[1];
  const url = `https://xivapi.com/character/${lodestoneId}?data=AC`;

  const response = await fetch(url);
  const data = await response.json();

  if (data.Error) {
    alert("Failed to retrieve achievements");
    return;
  }

  let achievements = data.Achievements;
  achievements = Object.values(achievements);
  console.log(achievements);
  
  // Sort the achievements in chronological order
  achievements.sort((a, b) => {
    const dateA = new Date(a.Date).getTime();
    const dateB = new Date(b.Date).getTime();
    return dateA - dateB;
  });

  return achievements;
}

export default getAchievements;
