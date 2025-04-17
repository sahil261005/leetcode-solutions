var compactObject = function (obj) {
  const isArray = Array.isArray(obj);
  const result = isArray ? [] : {};

  if (isArray) {
    for (let i = 0; i < obj.length; i++) {
      const el = obj[i];
      if (Array.isArray(el) || (el !== null && typeof el === "object"))
        result.push(compactObject(el));
      else if (el) result.push(el);
    }
  } else {
    for (let key in obj) {
      const el = obj[key];
      if (Array.isArray(el) || (el !== null && typeof el === "object"))
        result[key] = compactObject(el);
      else if (el) result[key] = el;
    }
  }

  return result;
};
