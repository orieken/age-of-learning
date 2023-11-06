#FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
#WORKDIR /App
#
## Copy everything
#COPY . ./
## Restore as distinct layers
#RUN dotnet restore
## Build and publish a release
#RUN dotnet publish -c Release -o out
#
## Build runtime image
#FROM mcr.microsoft.com/dotnet/aspnet:7.0
#WORKDIR /App
#COPY --from=build-env /App/out .
#ENTRYPOINT ["dotnet", "DotNet.Docker.dll"]

FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:7.0 AS build
ARG TARGETARCH
WORKDIR /source

# copy csproj and restore as distinct layers
COPY *.csproj .
RUN dotnet restore -a $TARGETARCH

# 
COPY . .
RUN dotnet test  -l "console;verbosity=normal" -a $TARGETARCH